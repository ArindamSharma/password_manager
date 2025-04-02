import 'package:flutter/material.dart';
import 'package:rudraksha/models/vault.dart';
import 'package:rudraksha/models/item.dart';
import 'package:rudraksha/screens/home/vault_list.dart';
import 'package:rudraksha/screens/home/item_list.dart';
import 'package:rudraksha/screens/home/item_detail.dart';

class HomePage extends StatefulWidget {
  final Function(bool) updateLoginState;
  final String username;

  const HomePage({super.key, required this.username, required this.updateLoginState});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late Widget _currentPage;
  String _currentTitle = 'Vaults';

  @override
  void initState() {
    super.initState();
    _currentPage = VaultList(
      navigateToItemList: _navigateToItemList,
    );
  }

  void _navigateToItemList() {
    setState(() {
      _currentTitle = 'Items';
      _currentPage = ItemList(
        navigateToItemDetail: _navigateToItemDetail,
      );
    });
  }

  void _navigateToItemDetail() {
    setState(() {
      _currentTitle = 'Item Detail';
      _currentPage = ItemDetail(
        navigateBackToItemList: _navigateBackToItemList,
      );
    });
  }

  void _navigateBackToItemList() {
    setState(() {
      _currentTitle = 'Items';
      _currentPage = ItemList(
        navigateToItemDetail: _navigateToItemDetail,
      );
    });
  }

  void _navigateBackToVaultList() {
    setState(() {
      _currentTitle = 'Vaults';
      _currentPage = VaultList(
        navigateToItemList: _navigateToItemList,
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_currentTitle),
        leading: _currentTitle == 'Vaults'
            ? null
            : IconButton(
                icon: const Icon(Icons.arrow_back),
                onPressed: _currentTitle == 'Items'
                    ? _navigateBackToVaultList
                    : _navigateBackToItemList,
              ),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              // Implement logout functionality
              widget.updateLoginState(false);
            },
            tooltip: 'Logout',
          ),
        ],
      ),
      body: _currentPage,
    );
  }
}