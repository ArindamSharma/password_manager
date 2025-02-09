import 'package:flutter/material.dart';
import '../colors.dart';

class BottomNavBar extends StatelessWidget {
  final int selectedIndex;
  final Function(int) onItemTapped;

  const BottomNavBar({
    required this.selectedIndex,
    required this.onItemTapped,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      items: const <BottomNavigationBarItem>[
        BottomNavigationBarItem(
          icon: Icon(Icons.home),
          label: 'Home',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.settings),
          label: 'Settings',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.web),
          label: 'Web',
        ),
      ],
      currentIndex: selectedIndex,
      onTap: onItemTapped,
      backgroundColor: primaryColor, // Set background color
      selectedItemColor: Colors.white,
      unselectedItemColor: Colors.grey,
    );
  }
}