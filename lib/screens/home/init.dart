import 'package:flutter/material.dart';
import 'login.dart';
import 'home.dart';

class HomeSection extends StatefulWidget {
  final String currentUser; //defined here to passing it to HomePage
  final bool isLoggedIn; //defined here to accessing the login state and open the HomePage or LoginPage
  final Function(bool, {String currentUser}) updateLoginState;

  const HomeSection({super.key,required this.currentUser, required this.isLoggedIn, required this.updateLoginState});

  @override
  _HomeSectionState createState() => _HomeSectionState();
}

class _HomeSectionState extends State<HomeSection> {
  @override
  Widget build(BuildContext context) {
    if (widget.isLoggedIn) {
      return HomePage(username: widget.currentUser,updateLoginState: widget.updateLoginState);
    } else {
      return LoginPage(updateLoginState: widget.updateLoginState);
    }
  }
}