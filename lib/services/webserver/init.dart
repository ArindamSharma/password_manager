import 'dart:io';
import 'package:Rudraksha/services/webserver/route.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart' as io;

class WebServer {
  HttpServer? _server;

  Future<void> start() async {
    final routes = Routes().router;

    // Create a handler
    final handler = const Pipeline()
        .addMiddleware(logRequests())
        .addHandler(routes);

    // Start the server
    _server = await io.serve(handler, InternetAddress.anyIPv4, 8080);
    print('Server listening on port ${_server!.port}');
  }

  Future<void> stop() async {
    if (_server != null) {
      await _server!.close(force: true);
      print('Server stopped');
    }
  }
}