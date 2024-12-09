import 'package:flutter/material.dart';
import '../main.dart';
import '../colors.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  String _toTitleCase(String text) {
    if (text.isEmpty) return text;
    return text.split(' ').map((word) {
      if (word.isEmpty) return word;
      return word[0].toUpperCase() + word.substring(1).toLowerCase();
    }).join(' ');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home', style: TextStyle(color: backgroundColor)),
        actions: [
          ValueListenableBuilder<String>(
            valueListenable: MyApp.username,
            builder: (context, username, child) {
              return Row(
                children: [
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 8.0),
                    child: Text(
                      _toTitleCase(username),
                      style: const TextStyle(color: backgroundColor, fontSize: 18, fontWeight: FontWeight.bold),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: IconButton(
                      icon: const Icon(Icons.logout, color: backgroundColor, size: 28),
                      onPressed: () {
                        MyApp.isLoggedIn.value = false;
                        MyApp.username.value = '';
                      },
                    ),
                  ),
                ],
              );
            },
          ),
        ],
      ),
      body: const Center(
        child: Text('Home Page', style: TextStyle(color: Colors.white)),
      ),
    );
  }
}