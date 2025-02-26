import 'package:flutter/material.dart';

class WebSection extends StatelessWidget {
  const WebSection({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Web Page'),
      ),
      body: Center(
        child: Text('Web Page', style: TextStyle(fontSize: 24)),
      ),
    );
  }
}