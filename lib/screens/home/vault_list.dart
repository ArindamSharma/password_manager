import 'package:flutter/material.dart';

class VaultList extends StatelessWidget {
  final VoidCallback navigateToItemList;

  const VaultList({super.key, required this.navigateToItemList});

  void _showAddVaultDialog(BuildContext context) {
    final TextEditingController titleController = TextEditingController();
    final TextEditingController descriptionController = TextEditingController();

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Add Vault'),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(
                  controller: titleController,
                  decoration: const InputDecoration(
                    labelText: 'Vault Title',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                TextField(
                  controller: descriptionController,
                  decoration: const InputDecoration(
                    labelText: 'Vault Description',
                    border: OutlineInputBorder(),
                  ),
                  maxLines: 3, // Allows multi-line input for the description
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop(); // Close the dialog
              },
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                // Implement the logic to add the vault
                print('Vault Added: ${titleController.text}, ${descriptionController.text}');
                Navigator.of(context).pop(); // Close the dialog
              },
              child: const Text('Add'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('No Vaults Found'),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: navigateToItemList,
              child: const Text('Go to Item List'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _showAddVaultDialog(context); // Show the dialog when the button is pressed
        },
        child: const Icon(Icons.add),
        tooltip: 'Add Vault',
      ),
    );
  }
}