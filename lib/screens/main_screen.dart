import 'package:flutter/material.dart';
import 'package:Rudraksha/screens/home/init.dart';
import 'package:Rudraksha/screens/setting/init.dart';
import 'package:Rudraksha/screens/web/init.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _selectedIndex = 0;
  final PageController _pageController = PageController();

  // Define the login state here because it is shared across the app sections and wont logout on section change
  bool isLoggedIn = false;
  String _currentUser='';

  void updateLoginState(bool value, {String currentUser = ''}) {
    setState(() {
      isLoggedIn = value;
      if(isLoggedIn){
        this._currentUser = currentUser;
      }
    });
  }
  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
    _pageController.jumpToPage(index);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView(
        scrollDirection: Axis.horizontal,
        controller: _pageController,
        onPageChanged: (index) {
          setState(() {
            _selectedIndex = index;
          });
        },
        children: <Widget>[
          HomeSection(isLoggedIn: isLoggedIn, currentUser: _currentUser, updateLoginState: updateLoginState),
          const SettingSection(),
          const WebSection(),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
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
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.blue,
        onTap: _onItemTapped,
      ),
    );
  }
}