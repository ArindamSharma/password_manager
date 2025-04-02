class Item {
  static const String tableName = 'Item';
  static const String columnId = 'id';
  static const String columnVaultId = 'vaultid';
  static const String columnTitle = 'title';
  static const String columnUsername = 'username';
  static const String columnPassword = 'password';
  static const String columnMetadata = 'metadata';
  static const String columnModifiedDATIME = 'modifieddatime';

  final int id;
  final int vaultid;
  final String title;
  final String username;
  final String password;
  final String? metadata;
  final String? modifieddatime;

  Item({
    required this.id,
    required this.vaultid,
    required this.title,
    required this.username,
    required this.password,
    this.metadata,
    this.modifieddatime,
  });

  // Convert a Item object into a Map object
  Map<String, dynamic> toMap() {
    return {
      columnId: id,
      columnVaultId: vaultid,
      columnTitle: title,
      columnUsername: username,
      columnPassword: password,
      columnMetadata: metadata,
      columnModifiedDATIME: modifieddatime,
    };
  }

  // Extract a Item object from a Map object
  factory Item.fromMap(Map<String, dynamic> map) {
    return Item(
      id: map[columnId],
      vaultid: map[columnVaultId],
      title: map[columnTitle],
      username: map[columnUsername],
      password: map[columnPassword],
      metadata: map[columnMetadata],
      modifieddatime: map[columnModifiedDATIME],
    );
  }
}