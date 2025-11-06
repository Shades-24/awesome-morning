#!/usr/bin/env python3
"""
Simple script to set your agenda for tomorrow morning.
Run this the night before to set what you want to accomplish.

Usage:
    python set_agenda.py
    (then type your agenda items, press Ctrl+D or Ctrl+Z when done)

Or:
    python set_agenda.py "Meeting at 9am, Gym at 5pm, Finish report"
"""

import sys
from agenda_manager import set_agenda, load_agenda

def main():
    print("=" * 60)
    print("SET YOUR AGENDA FOR TOMORROW")
    print("=" * 60)
    print()

    if len(sys.argv) > 1:
        # Agenda provided as command line argument
        agenda_text = ' '.join(sys.argv[1:])
    else:
        # Interactive mode
        print("Enter your agenda for tomorrow (press Ctrl+D or Ctrl+Z when done):")
        print("Example:")
        print("  - Morning workout at 6:30am")
        print("  - Team meeting at 10am")
        print("  - Lunch with client at 12pm")
        print("  - Finish project proposal")
        print()
        print("Your agenda:")

        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass

        agenda_text = '\n'.join(lines).strip()

    if not agenda_text:
        print("\n❌ No agenda entered. Try again!")
        return

    # Set the agenda
    print()
    if set_agenda(agenda_text):
        print()
        print("=" * 60)
        print("✓ SUCCESS! Your agenda is set for tomorrow morning!")
        print("=" * 60)
    else:
        print("\n❌ Failed to set agenda")

def show_agenda():
    """Show the current agenda."""
    print("=" * 60)
    print("CURRENT AGENDA")
    print("=" * 60)
    print()

    agenda = load_agenda()
    if agenda:
        print(agenda)
    else:
        print("No agenda set yet.")

    print()
    print("=" * 60)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'show':
        show_agenda()
    else:
        main()
