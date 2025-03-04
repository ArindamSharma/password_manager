import 'package:flutter/material.dart';
import 'package:flutter_passwordapp/models/item.dart';

class ItemDetailPage extends StatefulWidget {
  final int vaultId;
  final Item? item;
  final ValueChanged<Item>? onSave;

  const ItemDetailPage({super.key, required this.vaultId, this.item, this.onSave});

  @override
  _ItemDetailPageState createState() => _ItemDetailPageState();
}

class _ItemDetailPageState extends State<ItemDetailPage> {
  final TextEditingController titleController = TextEditingController();
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController metadataController = TextEditingController();

  @override
  void initState() {
    super.initState();
    titleController.text = widget.item!.title;
    usernameController.text = widget.item!.username;
    passwordController.text = widget.item!.password;
    metadataController.text = widget.item!.metadata!;
  }

  void _saveItem() {
    widget.onSave!(
      Item(
        id: widget.item!.id,
        title: titleController.text,
        username: usernameController.text,
        password: passwordController.text,
        metadata: metadataController.text,
        vaultid: widget.vaultId,
        modifieddatime: DateTime.now().toString(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TextField(
              controller: titleController,
              decoration: const InputDecoration(labelText: 'Title'),
            ),
            const SizedBox(height: 8),
            TextField(
              controller: usernameController,
              decoration: const InputDecoration(labelText: 'Username'),
            ),
            const SizedBox(height: 8),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
            ),
            const SizedBox(height: 8),
            TextField(
              controller: metadataController,
              decoration: const InputDecoration(labelText: 'Metadata'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _saveItem,
              child: const Text('Save'),
            ),
          ],
        ),
      ),
    );
  }
}