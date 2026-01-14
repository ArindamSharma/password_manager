import 'package:flutter/material.dart';

class ItemDetail extends StatelessWidget {
  final VoidCallback navigateBackToItemList;

  const ItemDetail({super.key, required this.navigateBackToItemList});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('No Details Available'),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: navigateBackToItemList,
              child: const Text('Back to Item List'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Implement edit item functionality
          print('Edit Item button pressed');
        },
        child: const Icon(Icons.edit),
        tooltip: 'Edit Item',
      ),
    );
  }
}