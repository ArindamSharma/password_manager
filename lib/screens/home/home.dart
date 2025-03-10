import 'package:flutter/material.dart';
import 'package:Rudraksha/models/vault.dart';
import 'package:Rudraksha/models/item.dart';
import 'package:Rudraksha/screens/home/vault_list.dart';
import 'package:Rudraksha/screens/home/item_list.dart';
import 'package:Rudraksha/screens/home/item_detail.dart';

class HomePage extends StatefulWidget {
  final Function(bool) updateLoginState;
  final String username;

  const HomePage({super.key, required this.username, required this.updateLoginState});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late Widget _currentPage;

  @override
  void initState() {
    super.initState();
    _currentPage = VaultList(
      username: widget.username,
      onVaultSelected: (vault) {
        setState(() {
          _currentPage = ItemList(
            vault: vault,
            onItemSelected: (item) {
              setState(() {
                _currentPage = ItemDetail(item: item);
              });
            },
          );
        });
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _currentPage,
    );
  }
}