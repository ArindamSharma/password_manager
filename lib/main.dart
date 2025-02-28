import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/screens/main_screen.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() async{
  WidgetsFlutterBinding.ensureInitialized(); // Ensure proper initialization

    // Check if the database has been initialized
  SharedPreferences prefs = await SharedPreferences.getInstance();
  bool isDatabaseInitialized = prefs.getBool('isDatabaseInitialized') ?? false;

  if (!isDatabaseInitialized) {
    await DatabaseService.refreshDatabase(); // Refresh the database
    await prefs.setBool('isDatabaseInitialized', true); // Set the flag to true
  }
  // await DatabaseService.printAllTables(); // Print all tables in the database
  
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
