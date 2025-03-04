String formatDateTime(String dateTime) {
  final DateTime parsedDateTime = DateTime.parse(dateTime);
  final String formattedDate = '${parsedDateTime.day.toString().padLeft(2, '0')}/${parsedDateTime.month.toString().padLeft(2, '0')}/${parsedDateTime.year} ${parsedDateTime.hour.toString().padLeft(2, '0')}:${parsedDateTime.minute.toString().padLeft(2, '0')}';
  return formattedDate;
}