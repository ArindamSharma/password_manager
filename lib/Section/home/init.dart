import 'package:flutter/material.dart';
import 'login.dart';
import 'home.dart';

class HomeSection extends StatefulWidget {
  final bool isLoggedIn;
  final Function(bool) updateLoginState;

  const HomeSection({
    super.key,
    required this.isLoggedIn,
    required this.updateLoginState,
  });

  @override
  _HomeSectionState createState() => _HomeSectionState();
}

class _HomeSectionState extends State<HomeSection> {
  @override
  Widget build(BuildContext context) {
    if (widget.isLoggedIn) {
      return HomePage(updateLoginState: widget.updateLoginState);
    } else {
      return LoginPage(updateLoginState: widget.updateLoginState);
    }
  }
}