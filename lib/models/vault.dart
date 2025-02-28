class Vault {
  static const String tableName = 'Vault';
  static const String columnId = 'id';
  static const String columnTitle = 'title';
  static const String columnUserID = 'userid';
  static const String columnDescription = 'description';
  static const String columnModifiedDATIME = 'modifieddatime';

  final int? id;
  final String title;
  final String userid;
  final String description;
  final String? modifieddatime;

  Vault({
    this.id,
    required this.title,
    required this.userid,
    required this.description,
    this.modifieddatime,
  });

  // Convert a Vault object into a Map object
  Map<String, dynamic> toMap() {
    return {
      columnId: id,
      columnTitle: title,
      columnUserID: userid,
      columnDescription: description,
      columnModifiedDATIME: modifieddatime,
    };
  }

  // Extract a Vault object from a Map object
  factory Vault.fromMap(Map<String, dynamic> map) {
    return Vault(
      id: map[columnId],
      title: map[columnTitle],
      userid: map[columnUserID],
      description: map[columnDescription],
      modifieddatime: map[columnModifiedDATIME],
    );
  }
}