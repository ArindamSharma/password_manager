import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/Section/MainScreen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized(); // Ensure proper initialization
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
