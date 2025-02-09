import 'package:flutter/material.dart';
import '../colors.dart';

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings', style: TextStyle(color: backgroundColor)),
      ),
      body: const Center(
        child: Text('Settings Page'),
      ),
    );
  }
}