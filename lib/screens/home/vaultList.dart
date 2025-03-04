import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/models/vault.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';
import 'package:flutter_passwordapp/utills/datetime.dart';

class VaultList extends StatefulWidget {
  final String username;
  final ValueChanged<Vault> onVaultSelected;

  const VaultList({super.key, required this.username, required this.onVaultSelected});

  @override
  _VaultListState createState() => _VaultListState();
}

class _VaultListState extends State<VaultList> {
  late Future<List<Vault>> _vaultsFuture;

  @override
  void initState() {
    super.initState();
    _vaultsFuture = _getVaults();
  }

  Future<List<Vault>> _getVaults() async {
    // Replace with the actual user ID of the signed-in user
    List<Vault> vaults = await DatabaseService.getVaultEntriesByUserId(widget.username);
    print('Vaults: $vaults');
    return vaults;
  }

  void _editVault(BuildContext context, Vault vault) {
    _showVaultDialog(context, vault: vault);
  }

  void _deleteVault(BuildContext context, int vaultid) async {
    try {
      await DatabaseService.deleteVault(vaultid);
      print('Vault deleted: $vaultid');
      // Refresh the vault list after deletion
      setState(() {
        _vaultsFuture = _getVaults();
      });
    } catch (e) {
      print('Error deleting vault: $e');
    }
  }

  void _saveVault(BuildContext context, {int? vaultid, required String title, required String description}) async {
    try {
      if (vaultid == null) {
        // Add new vault logic
        await DatabaseService.addVaultEntry(title, widget.username, description);
        print('Vault added: $title');
      } else {
        // Edit existing vault logic
        await DatabaseService.updateVault(vaultid, title, description);
        print('Vault updated: $title');
      }
      // Refresh the vault list after saving
      setState(() {
        _vaultsFuture = _getVaults();
      });
    } catch (e) {
      print('Error saving vault: $e');
    }
    Navigator.of(context).pop();
  }

  void _showVaultDialog(BuildContext context, {Vault? vault}) {
    final TextEditingController titleController = TextEditingController(text: vault?.title ?? '');
    final TextEditingController descriptionController = TextEditingController(text: vault?.description ?? '');

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Vault'),
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
              onPressed: () {
                _saveVault(
                  context,
                  vaultid: vault?.id,
                  title: titleController.text,
                  description: descriptionController.text,
                );
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
    return FutureBuilder<List<Vault>>(
      future: _vaultsFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Center(child: CircularProgressIndicator());
        } else if (snapshot.hasError) {
          return Center(child: Text('Error: ${snapshot.error}'));
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return const Center(child: Text('No vaults found.'));
        } else {
          return SingleChildScrollView(
            child: Wrap(
              spacing: 10,
              runSpacing: 10,
              children: snapshot.data!.map((vault) {
                return Card(
                  child: Column(
                    children: [
                      ListTile(
                        title: Text(vault.title),
                        subtitle: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(vault.description),
                            Text('Modified: ${formatDateTime(vault.modifieddatime ?? '')}'),
                          ],
                        ),
                        trailing: PopupMenuButton<String>(
                          onSelected: (value) {
                            if (value == 'edit') {
                              _editVault(context, vault);
                            } else if (value == 'delete') {
                              _deleteVault(context, vault.id!);
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
                        onTap: () => widget.onVaultSelected(vault),
                      ),
                      // Store the vault ID in a way that doesn't take up space
                      Container(
                        height: 0,
                        width: 0,
                        child: Text(
                          'ID: ${vault.id}',
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