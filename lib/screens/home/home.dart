import 'package:Rudraksha/models/vault.dart';
import 'package:flutter/material.dart';
import 'package:Rudraksha/services/database_service/init.dart';

class HomePage extends StatefulWidget {
  final Function(bool) updateLoginState;
  final String username;

  const HomePage({super.key, required this.username, required this.updateLoginState});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<Vault> _vaults = [];

  @override
  void initState() {
    super.initState();
    _fetchVaults();
  }

  Future<void> _fetchVaults() async {
    try {
      final vaults = await DatabaseService.getVaultEntriesByUserId(widget.username);
      setState(() {
        _vaults = vaults;
      });
    } catch (e) {
      print('Error fetching vaults: $e');
    }
  }

  void _addVault(BuildContext context) {
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
                  await DatabaseService.addVaultEntry(
                    titleController.text,
                    widget.username,
                    descriptionController.text,
                  );
                  print('Vault added: ${titleController.text}');
                  Navigator.of(context).pop();
                  _fetchVaults(); // Refresh the vault list
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Vaults'),
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
      body: _vaults.isEmpty
          ? Center(child: Text('Welcome, ${widget.username}!'))
          : ListView.builder(
              itemCount: _vaults.length,
              itemBuilder: (context, index) {
                final vault = _vaults[index];
                return ListTile(
                  leading: Icon(Icons.lock),
                  title: Text(vault.title),
                  onTap: () {
                    // Handle vault tap
                    print('Vault tapped: ${vault.title}');
                  },
                );
              },
            ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          _addVault(context);
        },
        icon: const Icon(Icons.add),
        label: const Text('Vault'),
        tooltip: 'Add Vault',
      ),
    );
  }
}