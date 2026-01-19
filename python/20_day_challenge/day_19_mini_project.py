"""
Day 19: Mini Project - CLI File Organizer
==========================================
Build a command-line file organizer using all concepts learned.

This project combines:
- File I/O (Day 1-2)
- JSON config (Day 3)
- CSV reports (Day 4)
- Error handling (Day 5)
- Logging (Day 6)
- Regex patterns (Day 7-8)
- Environment config (Day 9)
- CLI arguments (Day 10)
- Data validation (Day 14)
- Pathlib (Day 17)
- DateTime (Day 18)
"""

import argparse
import json
import csv
import logging
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_CONFIG = {
    "rules": [
        {"pattern": "*.jpg", "destination": "Images"},
        {"pattern": "*.png", "destination": "Images"},
        {"pattern": "*.pdf", "destination": "Documents"},
        {"pattern": "*.doc*", "destination": "Documents"},
        {"pattern": "*.mp3", "destination": "Music"},
        {"pattern": "*.mp4", "destination": "Videos"},
        {"pattern": "*.zip", "destination": "Archives"},
    ],
    "date_folders": False,
    "dry_run": False,
    "log_level": "INFO"
}


# =============================================================================
# LOGGING SETUP
# =============================================================================

def setup_logging(level="INFO", log_file=None):
    """Configure logging for the application."""
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=log_format,
        handlers=handlers
    )

    return logging.getLogger(__name__)


# =============================================================================
# FILE ORGANIZER CLASS
# =============================================================================

class FileOrganizer:
    """Main file organizer class."""

    def __init__(self, config=None, logger=None):
        """Initialize the organizer with config."""
        self.config = config or DEFAULT_CONFIG.copy()
        self.logger = logger or logging.getLogger(__name__)
        self.stats = {
            "scanned": 0,
            "moved": 0,
            "skipped": 0,
            "errors": 0,
            "by_destination": {}
        }
        self.history = []

    def load_config(self, config_path):
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            self.config.update(user_config)
            self.logger.info(f"Loaded config from {config_path}")
        except FileNotFoundError:
            self.logger.warning(f"Config not found: {config_path}, using defaults")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in config: {e}")
            raise

    def save_config(self, config_path):
        """Save current configuration to file."""
        with open(config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        self.logger.info(f"Saved config to {config_path}")

    def add_rule(self, pattern, destination):
        """Add a new organization rule."""
        rule = {"pattern": pattern, "destination": destination}
        self.config["rules"].append(rule)
        self.logger.debug(f"Added rule: {pattern} -> {destination}")

    def match_rule(self, filename):
        """Find matching rule for a filename."""
        for rule in self.config["rules"]:
            pattern = rule["pattern"]
            # Convert glob pattern to regex
            regex_pattern = pattern.replace(".", r"\.").replace("*", ".*")
            if re.match(regex_pattern, filename, re.IGNORECASE):
                return rule
        return None

    def get_destination(self, file_path, rule):
        """Get destination path for a file."""
        dest_folder = rule["destination"]

        if self.config.get("date_folders"):
            # Add date subfolder
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            dest_folder = Path(dest_folder) / mtime.strftime("%Y/%m")

        return dest_folder

    def organize_file(self, file_path, base_dir, dry_run=None):
        """Organize a single file."""
        file_path = Path(file_path)
        base_dir = Path(base_dir)
        dry_run = dry_run if dry_run is not None else self.config.get("dry_run", False)

        if not file_path.is_file():
            self.logger.debug(f"Skipping non-file: {file_path}")
            return None

        rule = self.match_rule(file_path.name)
        if not rule:
            self.logger.debug(f"No matching rule for: {file_path.name}")
            self.stats["skipped"] += 1
            return None

        dest_folder = self.get_destination(file_path, rule)
        dest_path = base_dir / dest_folder / file_path.name

        # Handle duplicate names
        if dest_path.exists():
            dest_path = self._get_unique_path(dest_path)

        try:
            if not dry_run:
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(dest_path))

            self.logger.info(f"{'[DRY RUN] Would move' if dry_run else 'Moved'}: "
                           f"{file_path.name} -> {dest_folder}")

            # Update stats
            self.stats["moved"] += 1
            dest_name = rule["destination"]
            self.stats["by_destination"][dest_name] = \
                self.stats["by_destination"].get(dest_name, 0) + 1

            # Record history
            self.history.append({
                "timestamp": datetime.now().isoformat(),
                "source": str(file_path),
                "destination": str(dest_path),
                "dry_run": dry_run
            })

            return dest_path

        except Exception as e:
            self.logger.error(f"Error moving {file_path}: {e}")
            self.stats["errors"] += 1
            return None

    def _get_unique_path(self, path):
        """Get unique path by adding number suffix."""
        counter = 1
        while path.exists():
            new_name = f"{path.stem}_{counter}{path.suffix}"
            path = path.with_name(new_name)
            counter += 1
        return path

    def organize_directory(self, source_dir, dry_run=None):
        """Organize all files in a directory."""
        source_dir = Path(source_dir)
        self.logger.info(f"Organizing directory: {source_dir}")

        if not source_dir.exists():
            raise FileNotFoundError(f"Directory not found: {source_dir}")

        for file_path in source_dir.iterdir():
            self.stats["scanned"] += 1
            self.organize_file(file_path, source_dir, dry_run)

        return self.stats

    def get_report(self):
        """Generate organization report."""
        return {
            "summary": self.stats,
            "history": self.history,
            "timestamp": datetime.now().isoformat()
        }

    def save_report(self, report_path, format="json"):
        """Save report to file."""
        report = self.get_report()

        if format == "json":
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)

        elif format == "csv":
            with open(report_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["timestamp", "source", "destination", "dry_run"])
                writer.writeheader()
                writer.writerows(self.history)

        self.logger.info(f"Saved report to {report_path}")

    def undo(self, history_path=None):
        """Undo the last organization (from history)."""
        history = self.history
        if history_path:
            with open(history_path, 'r') as f:
                history = json.load(f).get("history", [])

        undone = 0
        for entry in reversed(history):
            if entry.get("dry_run"):
                continue

            source = Path(entry["destination"])
            dest = Path(entry["source"])

            if source.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(source), str(dest))
                self.logger.info(f"Undone: {source} -> {dest}")
                undone += 1

        return undone


# =============================================================================
# CLI INTERFACE
# =============================================================================

def create_parser():
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        prog='file-organizer',
        description='Organize files into folders based on rules',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  file-organizer organize ~/Downloads
  file-organizer organize ~/Downloads --dry-run
  file-organizer organize ~/Downloads --config my-rules.json
  file-organizer add-rule "*.py" "Code"
  file-organizer show-config
  file-organizer undo --history report.json
        '''
    )

    parser.add_argument('--config', '-c', help='Configuration file path')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                       help='Increase verbosity')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # organize command
    org_parser = subparsers.add_parser('organize', help='Organize files in directory')
    org_parser.add_argument('directory', help='Directory to organize')
    org_parser.add_argument('--dry-run', '-n', action='store_true',
                           help='Show what would be done')
    org_parser.add_argument('--date-folders', action='store_true',
                           help='Organize by date')
    org_parser.add_argument('--report', '-r', help='Save report to file')
    org_parser.add_argument('--format', choices=['json', 'csv'], default='json',
                           help='Report format')

    # add-rule command
    rule_parser = subparsers.add_parser('add-rule', help='Add organization rule')
    rule_parser.add_argument('pattern', help='File pattern (e.g., *.pdf)')
    rule_parser.add_argument('destination', help='Destination folder')
    rule_parser.add_argument('--save', action='store_true',
                            help='Save to config file')

    # show-config command
    subparsers.add_parser('show-config', help='Show current configuration')

    # undo command
    undo_parser = subparsers.add_parser('undo', help='Undo last organization')
    undo_parser.add_argument('--history', help='History file to use')

    return parser


def main(args=None):
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args(args)

    # Setup logging
    log_level = "DEBUG" if args.verbose > 1 else "INFO" if args.verbose else "WARNING"
    logger = setup_logging(log_level)

    # Initialize organizer
    organizer = FileOrganizer(logger=logger)

    # Load config if specified
    if args.config:
        organizer.load_config(args.config)

    # Handle commands
    if args.command == 'organize':
        if args.date_folders:
            organizer.config["date_folders"] = True

        stats = organizer.organize_directory(args.directory, args.dry_run)

        print(f"\nOrganization complete!")
        print(f"  Scanned: {stats['scanned']}")
        print(f"  Moved: {stats['moved']}")
        print(f"  Skipped: {stats['skipped']}")
        print(f"  Errors: {stats['errors']}")

        if stats['by_destination']:
            print(f"\nBy destination:")
            for dest, count in stats['by_destination'].items():
                print(f"  {dest}: {count}")

        if args.report:
            organizer.save_report(args.report, args.format)

    elif args.command == 'add-rule':
        organizer.add_rule(args.pattern, args.destination)
        print(f"Added rule: {args.pattern} -> {args.destination}")

        if args.save and args.config:
            organizer.save_config(args.config)

    elif args.command == 'show-config':
        print(json.dumps(organizer.config, indent=2))

    elif args.command == 'undo':
        undone = organizer.undo(args.history)
        print(f"Undone {undone} operations")

    else:
        parser.print_help()

    return 0


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Enhanced Rules

    Extend the organizer to support:

    1. Regex patterns (not just glob):
       {"pattern": "IMG_\\d{4}\\.jpg", "destination": "Photos", "type": "regex"}

    2. Multiple conditions:
       {
         "conditions": [
           {"pattern": "*.jpg"},
           {"min_size": 1024000}  # > 1MB
         ],
         "destination": "LargePhotos"
       }

    3. Rule priority:
       Rules should have priority, higher priority rules match first.

    4. Dynamic destinations:
       {"pattern": "*", "destination": "{ext}/{year}/{month}"}
       Where {ext}, {year}, {month} are replaced with file properties.
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Watch Mode

    Add a watch mode that monitors a directory for new files:

    file-organizer watch ~/Downloads

    Features:
    - Organize new files automatically
    - Configurable delay before organizing (wait for downloads to complete)
    - Ignore list for temporary files
    - Status updates
    - Graceful shutdown (Ctrl+C)

    Hint: Use os.walk periodically or watchdog library
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Interactive Mode

    Add an interactive mode:

    file-organizer interactive ~/Downloads

    Shows each file and asks what to do:
    - [m]ove to suggested location
    - [s]kip
    - [d]elete
    - [c]ustom destination
    - [r]ename
    - [q]uit

    Include:
    - Preview of suggested organization
    - Batch operations (apply same action to matching files)
    - Search and filter
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Full-Featured File Manager

    Extend this into a complete file management system:

    1. Plugin System:
       - Load rules from plugins
       - Custom actions (compress, encrypt, upload)
       - Post-move hooks

    2. Cloud Integration:
       - Sync organized files to cloud storage
       - Download and organize from cloud

    3. Duplicate Detection:
       - Find duplicate files (by hash)
       - Options: keep newest, keep largest, keep all with suffix

    4. Smart Organization:
       - Use file metadata (EXIF for images, ID3 for music)
       - Content-based categorization (analyze text files)

    5. GUI (bonus):
       - Simple web interface to manage rules
       - Preview organizations
       - Real-time statistics

    6. Advanced Features:
       - Multi-threaded organization for large directories
       - Network drive support
       - Scheduled organization
       - Email reports
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 19: Mini Project - CLI File Organizer\n")
    print("=" * 50)

    # Demo mode if run directly
    print("""
This is a CLI tool. Run with --help for usage:

    python day_19_mini_project.py --help
    python day_19_mini_project.py organize ~/Downloads --dry-run
    python day_19_mini_project.py show-config

Or import and use programmatically:

    from day_19_mini_project import FileOrganizer

    organizer = FileOrganizer()
    organizer.add_rule("*.py", "Code")
    organizer.organize_directory("./downloads", dry_run=True)
    print(organizer.get_report())
    """)

    # Run demo
    import tempfile

    # Create demo directory
    demo_dir = Path(tempfile.mkdtemp())
    (demo_dir / "photo.jpg").touch()
    (demo_dir / "document.pdf").touch()
    (demo_dir / "song.mp3").touch()
    (demo_dir / "unknown.xyz").touch()

    print(f"\nDemo: Organizing {demo_dir}")
    print("-" * 40)

    organizer = FileOrganizer()
    organizer.organize_directory(demo_dir, dry_run=True)

    # Cleanup
    shutil.rmtree(demo_dir)
