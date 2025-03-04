import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/screens/home/itemlist.dart';
import 'package:flutter_passwordapp/screens/home/vaultlist.dart';
import 'package:flutter_passwordapp/models/vault.dart';
import 'package:flutter_passwordapp/models/item.dart';
import 'package:flutter_passwordapp/screens/home/itemDatails.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';

class HomePage extends StatefulWidget {
  final Function(bool) updateLoginState;
  final String username;

  const HomePage({super.key, required this.username, required this.updateLoginState});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  Vault? _selectedVault;
  Item? _selectedItem;

  void _showVaultList() {
    setState(() {
      _selectedVault = null;
      _selectedItem = null;
    });
  }

  void _showItemsPage(Vault vault) {
    setState(() {
      _selectedVault = vault;
      _selectedItem = null;
    });
  }

  void _showItemDetailPage(Item item) {
    setState(() {
      _selectedItem = item;
    });
  }

  void _addVault(BuildContext context) {
    final TextEditingController titleController = TextEditingController();
    final TextEditingController descriptionController = TextEditingController();

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Add Vault'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: titleController,
                decoration: const InputDecoration(labelText: 'Title'),
              ),
              TextField(
                controller: descriptionController,
                decoration: const InputDecoration(labelText: 'Description'),
              ),
            ],
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
                  await DatabaseService.addVaultEntry(
                    titleController.text,
                    widget.username,
                    descriptionController.text,
                  );
                  print('Vault added: ${titleController.text}');
                  Navigator.of(context).pop();
                  _showVaultList();
                } catch (e) {
                  print('Error adding vault: $e');
                }
              },
              child: const Text('Save'),
            ),
          ],
        );
      },
    );
  }

  void _addItem(BuildContext context) {
    setState(() {
      _selectedItem = Item(
        id: null,
        vaultid: _selectedVault!.id!,
        title: '',
        username: '',
        password: '',
        metadata: '',
      );
    });
  }

  void _saveItem(BuildContext context, Item item) async {
    try {
      if (item.id == null) {
        // Add new item logic
        await DatabaseService.addItem(
          item.vaultid,
          item.title,
          item.username,
          item.password,
          item.metadata!,
        );
        print('Item added: ${item.title}');
      } else {
        // Edit existing item logic
        await DatabaseService.updateItem(
          item.id!,
          item.title,
          item.username,
          item.password,
          item.metadata!,
        );
        print('Item updated: ${item.title}');
      }
      setState(() {
        _selectedItem = null;
      });
      _showItemsPage(_selectedVault!);
    } catch (e) {
      print('Error saving item: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_selectedItem != null
            ? '${_selectedItem!.title} Item'
            : _selectedVault != null
                ? '${_selectedVault!.title} Vault'
                : 'Vaults'),
        leading: _selectedVault != null
            ? IconButton(
                icon: const Icon(Icons.arrow_back),
                onPressed: () {
                  if (_selectedItem != null) {
                    setState(() {
                      _selectedItem = null;
                    });
                  } else {
                    _showVaultList();
                  }
                },
              )
            : null,
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
              // Add your search logic here
              print('Search button pressed');
            },
          ),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => widget.updateLoginState(false),
          ),
        ],
      ),
      body: _selectedItem != null
          ? ItemDetailPage(
              vaultId: _selectedVault!.id!,
              item: _selectedItem!,
              onSave: (item) => _saveItem(context, item),
            )
          : _selectedVault != null
              ? ItemsPage(
                  vaultId: _selectedVault!.id!,
                  vaultTitle: _selectedVault!.title,
                  onItemSelected: _showItemDetailPage,
                )
              : VaultList(
                  username: widget.username,
                  onVaultSelected: _showItemsPage,
                ),
      floatingActionButton: _selectedVault == null
          ? FloatingActionButton.extended(
              onPressed: () {
                _addVault(context);
              },
              icon: const Icon(Icons.add),
              label: const Text('Vault'),
              tooltip: 'Add Vault',
            )
          : FloatingActionButton.extended(
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