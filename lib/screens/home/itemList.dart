import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/screens/home/itemDatails.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';
import 'package:flutter_passwordapp/models/item.dart';
import 'package:flutter_passwordapp/utills/datetime.dart';

class ItemsPage extends StatefulWidget {
  final int vaultId;
  final String vaultTitle;
  final ValueChanged<Item> onItemSelected;

  const ItemsPage({super.key, required this.vaultId, required this.vaultTitle, required this.onItemSelected});

  @override
  _ItemsPageState createState() => _ItemsPageState();
}

class _ItemsPageState extends State<ItemsPage> {
  late Future<List<Item>> _itemsFuture;
  final TextEditingController _searchController = TextEditingController();
  List<Item> _allItems = [];
  List<Item> _filteredItems = [];

  @override
  void initState() {
    super.initState();
    _itemsFuture = _getItems();
  }

  Future<List<Item>> _getItems() async {
    List<Item> items = await DatabaseService.getItemsByVaultId(widget.vaultId.toString());
    print('Items: $items');
    _allItems = items;
    _filteredItems = items;
    return items;
  }

  void _editItem(BuildContext context, Item item) {
    _navigateToItemDetailPage(context, item: item);
  }

  void _deleteItem(BuildContext context, int itemId) async {
    try {
      await DatabaseService.deleteItem(itemId);
      print('Item deleted: $itemId');
      // Refresh the item list after deletion
      setState(() {
        _itemsFuture = _getItems();
      });
    } catch (e) {
      print('Error deleting item: $e');
    }
  }

  void _navigateToItemDetailPage(BuildContext context, {Item? item}) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ItemDetailPage(
          vaultId: widget.vaultId,
          item: item,
        ),
      ),
    );

    if (result == true) {
      // Refresh the item list after saving
      setState(() {
        _itemsFuture = _getItems();
      });
    }
  }

  void _filterItems(String query) {
    final filteredItems = _allItems.where((item) {
      final titleLower = item.title.toLowerCase();
      final usernameLower = item.username.toLowerCase();
      final searchLower = query.toLowerCase();

      return titleLower.contains(searchLower) || usernameLower.contains(searchLower);
    }).toList();

    setState(() {
      _filteredItems = filteredItems;
    });
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Item>>(
      future: _itemsFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Error: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return const Center(child: Text('No items found.'));
        } else {
          return SingleChildScrollView(
            child: Wrap(
              spacing: 10,
              runSpacing: 10,
              children: _filteredItems.map((item) {
                return Card(
                  child: Column(
                    children: [
                      ListTile(
                        title: Text(item.title),
                        subtitle: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(item.username),
                            Text('Modified: ${formatDateTime(item.modifieddatime ?? '')}'),
                          ],
                        ),
                        trailing: PopupMenuButton<String>(
                          onSelected: (value) {
                            if (value == 'edit') {
                              _editItem(context, item);
                            } else if (value == 'delete') {
                              _deleteItem(context, item.id!);
                            }
                          },
                          itemBuilder: (BuildContext context) {
                            return [
                              const PopupMenuItem<String>(
                                value: 'edit',
                                child: Text('Edit'),
                              ),
                              const PopupMenuItem<String>(
                                value: 'delete',
                                child: Text('Delete'),
                              ),
                            ];
                          },
                        ),
                        onTap: () => widget.onItemSelected(item),
                      ),
                      // Store the item ID in a way that doesn't take up space
                      Container(
                        height: 0,
                        width: 0,
                        child: Text(
                          'ID: ${item.id}',
                          style: const TextStyle(color: Colors.transparent),
                        ),
                      ),
                    ],
                  ),
                );
              }).toList(),
            ),
          );
        }
      },
    );
  }
}