import 'package:flutter/material.dart';
import '../main.dart';
import '../setting/setting.dart';
import '../web/web.dart';
import '../widgets/nav.dart';
import '../colors.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  bool _isSignUp = false;
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  String? _emailError;
  String? _usernameError;
  String? _passwordError;
  int _selectedIndex = 0; // Define the _selectedIndex variable

  void _validateInputs() {
    setState(() {
      _emailError = null;
      _usernameError = null;
      _passwordError = null;

      if (_isSignUp && _emailController.text.isEmpty) {
        _emailError = 'Email is required';
      } else if (_isSignUp && !RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(_emailController.text)) {
        _emailError = 'Invalid email format';
      }

      if (_usernameController.text.isEmpty) {
        _usernameError = 'Username is required';
      }

      if (_passwordController.text.isEmpty) {
        _passwordError = 'Password is required';
      }

      if (!_isSignUp && _usernameController.text == 'admin' && _passwordController.text == 'admin') {
        // Successful login
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Login successful')),
        );
        MyApp.isLoggedIn.value = true;
        MyApp.username.value = _usernameController.text;
      } else if (!_isSignUp) {
        // Invalid login
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Invalid username or password')),
        );
      }
    });
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    final List<Widget> _pages = <Widget>[
      LoginPageContent(
        isSignUp: _isSignUp,
        emailController: _emailController,
        usernameController: _usernameController,
        passwordController: _passwordController,
        emailError: _emailError,
        usernameError: _usernameError,
        passwordError: _passwordError,
        validateInputs: _validateInputs,
        onSignUpChanged: (value) {
          setState(() {
            _isSignUp = value;
          });
        },
      ),
      const SettingsPage(),
      const WebPage(),
    ];

    return Scaffold(
      body: _pages[_selectedIndex],
      bottomNavigationBar: BottomNavBar(
        selectedIndex: _selectedIndex,
        onItemTapped: _onItemTapped,
      ),
    );
  }
}

class LoginPageContent extends StatelessWidget {
  final bool isSignUp;
  final TextEditingController emailController;
  final TextEditingController usernameController;
  final TextEditingController passwordController;
  final String? emailError;
  final String? usernameError;
  final String? passwordError;
  final Function() validateInputs;
  final Function(bool) onSignUpChanged;

  const LoginPageContent({
    required this.isSignUp,
    required this.emailController,
    required this.usernameController,
    required this.passwordController,
    required this.emailError,
    required this.usernameError,
    required this.passwordError,
    required this.validateInputs,
    required this.onSignUpChanged,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: 50), // Adjust this value to move the message up
            const Text(
              'Welcome to Vault',
              style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold), // Increased font size
            ),
            const SizedBox(height: 8),
            const Text(
              'Advance Password Management Tool',
              style: TextStyle(fontSize: 16),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 16),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text('Sign In'),
                  Switch(
                    value: isSignUp,
                    onChanged: onSignUpChanged,
                    activeColor: accentColor,
                    activeTrackColor: secondaryColor,
                  ),
                  const Text('Sign Up'),
                ],
              ),
            ),
            if (isSignUp)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 16.0),
                child: SizedBox(
                  width: 300,
                  child: TextField(
                    controller: emailController,
                    decoration: InputDecoration(
                      labelText: 'Email',
                      border: const OutlineInputBorder(
                        borderSide: BorderSide(color: secondaryColor),
                      ),
                      focusedBorder: const OutlineInputBorder(
                        borderSide: BorderSide(color: accentColor),
                      ),
                      labelStyle: const TextStyle(color: primaryColor),
                      errorText: emailError,
                    ),
                    cursorColor: accentColor, // Set cursor color
                  ),
                ),
              ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: SizedBox(
                width: 300,
                child: TextField(
                  controller: usernameController,
                  decoration: InputDecoration(
                    labelText: 'Username',
                    border: const OutlineInputBorder(
                      borderSide: BorderSide(color: secondaryColor),
                    ),
                    focusedBorder: const OutlineInputBorder(
                      borderSide: BorderSide(color: accentColor),
                    ),
                    labelStyle: const TextStyle(color: primaryColor),
                    errorText: usernameError,
                  ),
                  cursorColor: accentColor, // Set cursor color
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: SizedBox(
                width: 300,
                child: TextField(
                  controller: passwordController,
                  decoration: InputDecoration(
                    labelText: 'Password',
                    border: const OutlineInputBorder(
                      borderSide: BorderSide(color: secondaryColor),
                    ),
                    focusedBorder: const OutlineInputBorder(
                      borderSide: BorderSide(color: accentColor),
                    ),
                    labelStyle: const TextStyle(color: primaryColor),
                    errorText: passwordError,
                  ),
                  obscureText: true,
                  cursorColor: accentColor, // Set cursor color
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: SizedBox(
                width: 300,
                child: ElevatedButton(
                  onPressed: validateInputs,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: secondaryColor,
                    foregroundColor: Colors.white, // Set text color
                  ),
                  child: const Text('Continue'),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}