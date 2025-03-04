import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/screens/main_screen.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() async{
  WidgetsFlutterBinding.ensureInitialized(); // Ensure proper initialization

  // Check if the app has been run before
  SharedPreferences prefs = await SharedPreferences.getInstance();
  bool isFirstRun = prefs.getBool('isFirstRun') ?? true;

  if (isFirstRun) {
    // Perform initial setup tasks
    await DatabaseService.refreshDatabase(); // Refresh the database
    await prefs.setBool('isFirstRun', false); // Set the flag to false
  } else {
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
