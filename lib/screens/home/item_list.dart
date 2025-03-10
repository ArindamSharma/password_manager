import 'package:flutter/material.dart';
import 'package:Rudraksha/models/item.dart';
import 'package:Rudraksha/models/vault.dart';
import 'package:Rudraksha/services/database_service/init.dart';

class ItemList extends StatefulWidget {
  final Vault vault;
  final Function(Item) onItemSelected;

  const ItemList({super.key, required this.vault, required this.onItemSelected});

  @override
  _ItemListState createState() => _ItemListState();
}

class _ItemListState extends State<ItemList> {
  List<Item> _items = [];

  @override
  void initState() {
    super.initState();
    _fetchItems();
  }

  Future<void> _fetchItems() async {
    try {
      final items = await DatabaseService.getItemsByVaultId(widget.vault.id);
      setState(() {
        _items = items;
      });
    } catch (e) {
      print('Error fetching items: $e');
    }
  }

  void _addItem(BuildContext context) {
    final TextEditingController titleController = TextEditingController();
    final TextEditingController descriptionController = TextEditingController();

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Add Item'),
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
                TextFormField(
                  controller: descriptionController,
                  decoration: const InputDecoration(
                    labelText: 'Description',
                    border: OutlineInputBorder(),
                  ),
                  maxLines: 5, // Allows the description to be a multi-line paragraph
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
                  await DatabaseService.addItem(
                    widget.vault.id,
                    titleController.text,
                    descriptionController.text,
                  );
                  print('Item added: ${titleController.text}');
                  Navigator.of(context).pop();
                  _fetchItems(); // Refresh the item list
                } catch (e) {
                  print('Error adding item: $e');
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
        title: Text(widget.vault.title),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () => Navigator.of(context).pop(),
        ),
      ),
      body: _items.isEmpty
          ? Center(child: Text('No items found'))
          : ListView.builder(
              itemCount: _items.length,
              itemBuilder: (context, index) {
                final item = _items[index];
                return ListTile(
                  leading: Icon(Icons.note),
                  title: Text(item.title),
                  onTap: () {
                    widget.onItemSelected(item);
                  },
                );
              },
            ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          _addItem(context);
        },
        icon: const Icon(Icons.add),
        label: const Text('Item'),
        tooltip: 'Add Item',
      ),
    );
  }
}