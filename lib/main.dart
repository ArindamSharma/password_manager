import 'package:flutter/material.dart';
import 'package:rudraksha/screens/main_screen.dart';
import 'package:rudraksha/services/database_service/init.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() async{
  WidgetsFlutterBinding.ensureInitialized(); // Ensure proper initialization

  // Check if the app has been run before
  SharedPreferences prefs = await SharedPreferences.getInstance();
  bool isFirstRun = prefs.getBool('isFirstRun') ?? true;

  if (isFirstRun) {
    print("First run detected");
    // Perform initial setup tasks
    await DatabaseService.refreshDatabase(); // Refresh the database
    await prefs.setBool('isFirstRun', false); // Set the flag to false
  } else {
    print("Subsequent run detected");
    await DatabaseService.database; // Ensure the database is initialized
  }

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MainScreen(),
      debugShowCheckedModeBanner: false, // Add this line to remove the debug label
    );
  }
}
