# Password Manager

Welcome to the Password Manager, a secure tool designed to manage your passwords efficiently. This application allows you to store passwords in vaults, ensuring that each vault is accessible only with a private key, providing an extra layer of security.

This is a Flutter project aimed at providing a robust and user-friendly password management solution.

## Development Commands

Here are some essential commands to help you build, test, and run your Flutter application:

### Build the Application

To build the application for release, use the following command:

```bash
flutter build apk --release
```
### Run the Application
To run the application on a specific device, such as Microsoft Edge, use:
```bash
flutter run -d edge
```
### Test the Application
To execute tests for your Flutter application, use:
```bash
flutter test
```
### Install flutter Environment without installing Android Studio

https://youtu.be/Sp__3Df22s8?feature=shared

Windows Steps: 
First download cmdline-tools zip > Extract > Open terminal (same location as of cmdline-tools/bin/)

```
sdkmanager.bat "build-tools:latest" --sdk_root="<new_location_for_sdk>"
```
and download platform-tools from here > https://developer.android.com/tools/releases/platform-tools

```
sdkmanager.bat "platform:30.0.0" --sdk_root="<new_location_for_sdk>"
```
```
sdkmanager.bat "cmdline-tools:latest" --sdk_root="<new_location_for_sdk>"
```
once all 4 items are installed/downloaded > update environment variable for plarform and platform-tools

Update the folder structure by 
```
flutter create .
```

Note: Make sure to have all <new_location_for_sdk> same.