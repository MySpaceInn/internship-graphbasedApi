// import 'dart:io';
// import 'package:intl/intl.dart';

// class Roster {
//   String name;
//   DateTime date;
//   String timeSlot;

//   Roster({required this.name, required this.date, required this.timeSlot});

//   @override
//   String toString() {
//     final dateFormat = DateFormat.yMd().format(date);
//     return 'Name: $name, Date: $datezFormat, Time Slot: $timeSlot';
//   }
// }

// List<Roster> rosters = [];

// void createRoster() {
//   stdout.write('Enter name: ');
//   String? name = stdin.readLineSync();

//   stdout.write('Enter date (MM/DD/YYYY): ');
//   String? dateString = stdin.readLineSync();
//   DateTime date = DateFormat('MM/dd/yyyy').parse(dateString!);

//   stdout.write('Enter time slot (12:6, 6:12): ');
//   String? timeSlot = stdin.readLineSync();

//   if (name != null && timeSlot != null) {
//     Roster newRoster = Roster(name: name, date: date, timeSlot: timeSlot);
//     rosters.add(newRoster);
//     print('Roster created successfully!');
//   } else {
//     print('Invalid input. Roster creation failed.');
//   }
// }

// void readRosters() {
//   if (rosters.isEmpty) {
//     print('No rosters available.');
//   } else {
//     for (int i = 0; i < rosters.length; i++) {
//       print('[$i] ${rosters[i]}');
//     }
//   }
// }

// void updateRoster() {
//   readRosters();
//   stdout.write('Enter the index of the roster to update: ');
//   String? indexString = stdin.readLineSync();
//   int index = int.parse(indexString!);

//   if (index >= 0 && index < rosters.length) {
//     stdout.write('Enter new name (leave empty to keep current): ');
//     String? newName = stdin.readLineSync();

//     stdout.write('Enter new date (MM/DD/YYYY, leave empty to keep current): ');
//     String? newDateString = stdin.readLineSync();
//     DateTime? newDate;
//     if (newDateString != null && newDateString.isNotEmpty) {
//       newDate = DateFormat('MM/dd/yyyy').parse(newDateString);
//     }

//     stdout.write(
//         'Enter new time slot (12:6, 6:12, leave empty to keep current): ');
//     String? newTimeSlot = stdin.readLineSync();

//     Roster roster = rosters[index];
//     roster.name = newName != null && newName.isNotEmpty ? newName : roster.name;
//     roster.date = newDate ?? roster.date;
//     roster.timeSlot = newTimeSlot != null && newTimeSlot.isNotEmpty
//         ? newTimeSlot
//         : roster.timeSlot;

//     print('Roster updated successfully!');
//   } else {
//     print('Invalid index. Roster update failed.');
//   }
// }

// void deleteRoster() {
//   readRosters();
//   stdout.write('Enter the index of the roster to delete: ');
//   String? indexString = stdin.readLineSync();
//   int index = int.parse(indexString!);

//   if (index >= 0 && index < rosters.length) {
//     rosters.removeAt(index);
//     print('Roster deleted successfully!');
//   } else {
//     print('Invalid index. Roster deletion failed.');
//   }
// }

// void main() {
//   while (true) {
//     print('\nRoster Management System');
//     print('1. Create Roster');
//     print('2. Read Rosters');
//     print('3. Update Roster');
//     print('4. Delete Roster');
//     print('5. Exit');
//     stdout.write('Enter your choice: ');
//     String? choice = stdin.readLineSync();

//     switch (choice) {
//       case '1':
//         createRoster();
//         break;
//       case '2':
//         readRosters();
//         break;
//       case '3':
//         updateRoster();
//         break;
//       case '4':
//         deleteRoster();
//         break;
//       case '5':
//         exit(0);
//       default:
//         print('Invalid choice. Please try again.');
//     }
//   }
// }
