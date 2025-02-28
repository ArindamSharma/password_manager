import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  final Function(bool) updateLoginState;

  const HomePage({super.key, required this.updateLoginState});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Page'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => updateLoginState(false),
          ),
        ],
      ),
      body: Center(
        child: Text('Home Page', style: TextStyle(fontSize: 24)),
      ),
      floatingActionButton: Align(
        alignment: Alignment.bottomLeft,
        child: FloatingActionButton(
          onPressed: () {
            // Add your logic to add a vault here
            print('Add Vault button pressed');
          },
          child: const Icon(Icons.add),
          tooltip: 'Add Vault',
        ),
      ),
    );
  }
}