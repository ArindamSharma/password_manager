import 'package:flutter/material.dart';

class ItemList extends StatelessWidget {
  final VoidCallback navigateToItemDetail;

  const ItemList({super.key, required this.navigateToItemDetail});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('No Items Found'),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: navigateToItemDetail,
              child: const Text('Go to Item Detail'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Implement add item functionality
          print('Add Item button pressed');
        },
        child: const Icon(Icons.add),
        tooltip: 'Add Item',
      ),
    );
  }
}