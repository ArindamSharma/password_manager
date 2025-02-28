import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/services/database_service/init.dart';
import 'package:flutter_passwordapp/models/vault.dart';

class HomePage extends StatelessWidget {
  final Function(bool) updateLoginState;
  final String username;

  const HomePage({super.key, required this.username, required this.updateLoginState});

  Future<List<Vault>> _getVaults() async {
    // Replace with the actual user ID of the signed-in user
    return await DatabaseService.getVaultEntriesByUserId(username);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(username),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => updateLoginState(false),
          ),
        ],
      ),
      body: FutureBuilder<List<Vault>>(
        future: _getVaults(),
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
                          subtitle: Text(vault.description),
                        ),
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: Text('Modified: ${vault.modifieddatime}'),
                        ),
                      ],
                    ),
                  );
                }).toList(),
              ),
            );
          }
        },
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          // Add your logic to add a vault here
          print('Add Vault button pressed');
        },
        icon: const Icon(Icons.add),
        label: const Text('Vault'),
        tooltip: 'Add Vault',
      ),
    );
  }
}