class User {
  static const String tableName = 'User';
  static const String columnId = 'id';
  static const String columnUsername = 'username';
  static const String columnPassword = 'password';
  static const String columnEmail = 'email';
  static const String columnModifiedDATIME = 'modifieddatime';

  final int? id;
  final String username;
  final String password;
  final String email;
  final String? modifieddatime;

  User({
    this.id,
    required this.username,
    required this.password,
    required this.email,
    this.modifieddatime,
  });

  // Convert a User object into a Map object
  Map<String, dynamic> toMap() {
    return {
      columnId: id,
      columnUsername: username,
      columnPassword: password,
      columnEmail: email,
      columnModifiedDATIME: modifieddatime,
    };
  }

  // Extract a User object from a Map object
  factory User.fromMap(Map<String, dynamic> map) {
    return User(
      id: map[columnId],
      username: map[columnUsername],
      password: map[columnPassword],
      email: map[columnEmail],
      modifieddatime: map[columnModifiedDATIME],
    );
  }
}