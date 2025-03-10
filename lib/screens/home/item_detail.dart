import 'package:flutter/material.dart';
import 'package:Rudraksha/models/item.dart';
import 'package:Rudraksha/services/database_service/init.dart';

class ItemDetail extends StatelessWidget {
  final Item item;

  const ItemDetail({super.key, required this.item});

  void _editItem(BuildContext context) {
    final TextEditingController titleController = TextEditingController(text: item.title);
    final TextEditingController usernameController = TextEditingController(text: item.username);
    final TextEditingController passwordController = TextEditingController(text: item.password);
    final TextEditingController metadataController = TextEditingController(text: item.metadata);

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Edit Item'),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(
                  controller: titleController,
                  decoration: const InputDecoration(
                    labelText: 'Title',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                TextField(
                  controller: usernameController,
                  decoration: const InputDecoration(
                    labelText: 'Username',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                TextField(
                  controller: passwordController,
                  decoration: const InputDecoration(
                    labelText: 'Password',
                    border: OutlineInputBorder(),
                  ),
                  obscureText: true,
                ),
                const SizedBox(height: 10),
                TextFormField(
                  controller: metadataController,
                  decoration: const InputDecoration(
                    labelText: 'Metadata',
                    border: OutlineInputBorder(),
                  ),
                  maxLines: 5, // Allows the metadata to be a multi-line paragraph
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () async {
                try {
                  await DatabaseService.updateItem(
                    item.id,
                    titleController.text,
                    usernameController.text,
                    passwordController.text,
                    metadataController.text,
                  );
                  print('Item updated: ${item.id}');
                  Navigator.of(context).pop();
                } catch (e) {
                  print('Error updating item: $e');
                }
              },
              child: const Text('Save'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(item.title),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () => Navigator.of(context).pop(),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              item.title,
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Text(
              'Username: ${item.username}',
              style: TextStyle(fontSize: 16),
            ),
            const SizedBox(height: 10),
            Text(
              'Password: ${item.password}',
              style: TextStyle(fontSize: 16),
            ),
            const SizedBox(height: 10),
            Text(
              'Metadata: ${item.metadata}',
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          _editItem(context);
        },
        icon: const Icon(Icons.edit),
        label: const Text('Edit'),
        tooltip: 'Edit Item',
      ),
    );
  }
}