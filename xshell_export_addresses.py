#!/usr/bin/env python3
"""
Xshell Sessions Address Exporter
=================================

This script helps export all host addresses from Xshell session files.
It searches for .xsh files in common Xshell directories and extracts connection information.

Author: Background Agent
"""

import os
import sys
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import csv
import argparse
from datetime import datetime


class XshellSessionExporter:
    def __init__(self):
        self.sessions = []
        self.common_paths = self._get_xshell_paths()
    
    def _get_xshell_paths(self):
        """Get common Xshell session file paths"""
        paths = []
        
        # Windows paths for different Xshell versions
        appdata = os.environ.get('APPDATA', '')
        if appdata:
            # Xshell 7/8
            paths.extend([
                os.path.join(appdata, 'NetSarang', 'Xshell', 'Sessions'),
                os.path.join(appdata, 'Netsarang Computer', '7', 'Xshell', 'Sessions'),
                os.path.join(appdata, 'Netsarang Computer', '8', 'Xshell', 'Sessions'),
            ])
            
            # Xshell 6 and earlier
            paths.extend([
                os.path.join(appdata, 'Netsarang Computer', '6', 'Xshell', 'Sessions'),
                os.path.join(appdata, 'NetSarang', 'Xshell', 'Sessions'),
                os.path.join(appdata, 'NetSarang Computer', 'Xshell', 'Sessions'),
            ])
        
        # Documents folder (alternative location)
        documents = os.path.expanduser('~/Documents')
        paths.extend([
            os.path.join(documents, 'NetSarang', 'Xshell', 'Sessions'),
            os.path.join(documents, 'Netsarang Computer', 'Xshell', 'Sessions'),
        ])
        
        # Current directory
        paths.append(os.getcwd())
        
        return [p for p in paths if os.path.exists(p)]
    
    def find_session_files(self, custom_path=None):
        """Find all .xsh session files"""
        session_files = []
        
        search_paths = [custom_path] if custom_path else self.common_paths
        
        for path in search_paths:
            if not os.path.exists(path):
                continue
                
            print(f"Searching in: {path}")
            
            # Search for .xsh files recursively
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith('.xsh'):
                        session_files.append(os.path.join(root, file))
        
        return session_files
    
    def parse_session_file(self, file_path):
        """Parse a single .xsh session file"""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            session_info = {
                'file_path': file_path,
                'file_name': os.path.basename(file_path),
                'session_name': '',
                'host': '',
                'port': '',
                'protocol': '',
                'username': '',
                'description': ''
            }
            
            # Extract session information
            for elem in root.iter():
                if elem.tag == 'Session':
                    session_info['session_name'] = elem.get('name', os.path.splitext(session_info['file_name'])[0])
                elif elem.tag == 'Connection':
                    for child in elem:
                        if child.tag == 'Host':
                            session_info['host'] = child.text or ''
                        elif child.tag == 'Port':
                            session_info['port'] = child.text or ''
                        elif child.tag == 'Protocol':
                            session_info['protocol'] = child.text or ''
                        elif child.tag == 'Description':
                            session_info['description'] = child.text or ''
                elif elem.tag == 'Authentication':
                    for child in elem:
                        if child.tag == 'UserName':
                            session_info['username'] = child.text or ''
            
            return session_info
            
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def export_sessions(self, custom_path=None):
        """Export all session information"""
        session_files = self.find_session_files(custom_path)
        
        if not session_files:
            print("No Xshell session files found!")
            print("Searched in the following directories:")
            for path in self.common_paths:
                print(f"  - {path}")
            return []
        
        print(f"Found {len(session_files)} session files")
        
        for file_path in session_files:
            session_info = self.parse_session_file(file_path)
            if session_info and session_info['host']:
                self.sessions.append(session_info)
        
        return self.sessions
    
    def save_to_csv(self, filename=None):
        """Save sessions to CSV file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"xshell_sessions_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['session_name', 'host', 'port', 'protocol', 'username', 'description', 'file_path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for session in self.sessions:
                writer.writerow(session)
        
        print(f"Sessions exported to: {filename}")
        return filename
    
    def save_to_json(self, filename=None):
        """Save sessions to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"xshell_sessions_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(self.sessions, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"Sessions exported to: {filename}")
        return filename
    
    def save_to_txt(self, filename=None):
        """Save sessions to simple text file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"xshell_addresses_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as txtfile:
            txtfile.write("Xshell Session Addresses Export\n")
            txtfile.write("=" * 40 + "\n\n")
            
            for session in self.sessions:
                txtfile.write(f"Session: {session['session_name']}\n")
                txtfile.write(f"Host: {session['host']}\n")
                if session['port']:
                    txtfile.write(f"Port: {session['port']}\n")
                if session['protocol']:
                    txtfile.write(f"Protocol: {session['protocol']}\n")
                if session['username']:
                    txtfile.write(f"Username: {session['username']}\n")
                if session['description']:
                    txtfile.write(f"Description: {session['description']}\n")
                txtfile.write(f"File: {session['file_path']}\n")
                txtfile.write("-" * 40 + "\n\n")
        
        print(f"Sessions exported to: {filename}")
        return filename
    
    def print_summary(self):
        """Print a summary of found sessions"""
        if not self.sessions:
            print("No sessions with host information found.")
            return
        
        print(f"\nFound {len(self.sessions)} sessions with host information:")
        print("=" * 60)
        
        for i, session in enumerate(self.sessions, 1):
            print(f"{i:3d}. {session['session_name']}")
            print(f"     Host: {session['host']}")
            if session['port']:
                print(f"     Port: {session['port']}")
            if session['protocol']:
                print(f"     Protocol: {session['protocol']}")
            if session['username']:
                print(f"     Username: {session['username']}")
            print()


def main():
    parser = argparse.ArgumentParser(description='Export Xshell session addresses')
    parser.add_argument('--path', '-p', help='Custom path to search for session files')
    parser.add_argument('--format', '-f', choices=['csv', 'json', 'txt', 'all'], 
                       default='all', help='Output format (default: all)')
    parser.add_argument('--output', '-o', help='Output filename (without extension)')
    parser.add_argument('--quiet', '-q', action='store_true', 
                       help='Only show summary, no detailed output')
    
    args = parser.parse_args()
    
    exporter = XshellSessionExporter()
    
    print("Xshell Sessions Address Exporter")
    print("=" * 40)
    
    # Export sessions
    sessions = exporter.export_sessions(args.path)
    
    if not sessions:
        print("\nNo sessions found. Please ensure:")
        print("1. Xshell is installed and has been used")
        print("2. Session files exist in the default locations")
        print("3. Or specify a custom path with --path")
        return
    
    # Print summary
    if not args.quiet:
        exporter.print_summary()
    
    # Save to requested formats
    if args.format in ['csv', 'all']:
        output_file = f"{args.output}.csv" if args.output else None
        exporter.save_to_csv(output_file)
    
    if args.format in ['json', 'all']:
        output_file = f"{args.output}.json" if args.output else None
        exporter.save_to_json(output_file)
    
    if args.format in ['txt', 'all']:
        output_file = f"{args.output}.txt" if args.output else None
        exporter.save_to_txt(output_file)
    
    print(f"\nExport completed! Found {len(sessions)} sessions.")


if __name__ == "__main__":
    main()