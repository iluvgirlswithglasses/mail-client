
# Manual

This section provides an overview of the features available in the interface.

Constants like server's host, server's port,... are not configurable within the interface. To change these constants, refer to config.json.

## Login Scene

In the login scene, users encounter the following interface:

![Login Scene](./img/login-0.png)

Since the test mail server doesn't require passwords, users only need to input their username.

![Typing in an address in the Login Scene](./img/login-1.png)

Upon successful login, users are directed to the menu scene.

## Menu Scene

Upon logging in, users are greeted with the menu scene:

![Menu Scene](./img/menu-0.png)

## Mail Composing Scene

Let's explore the mail composing scene. This interface allows users to interactively compose and send emails:

![Composing an Email](./img/mailcomposer-0.png)

Users can specify recipients in the TO, CC, and BCC fields, attach files, and adhere to attachment size limits:

![Attachment size limit, in a different color palette!](./img/mailcomposer-1.png)

## Mail Receiver Interface

Upon selecting the inbox from the menu, users are presented with the mail receiver interface:

![Mail Box](./img/inbox-0.png)

Users can specify the directory to view. When downloading a mail, the client automatically selects an appropriate directory based on the mail's content. The directory viewer interface is as follows:

![Mail Directory](./img/inbox-1.png)

New mails are marked as `[NEW]`, and the interface refreshes at intervals specified in config.json, eliminating concerns about missing emails.

## Mail Viewer

The mail viewer interface is displayed when users open an email:

![Mail Viewer](./img/mailviewer-0.png)

If the email has attachments, users can choose to save them. This operation strictly adheres to the project description:

![Saving an attachment](./img/mailviewer-1.png)

For emails with multiple attachments, users can save them individually:

![Saving multiple attachments](./img/mailviewer-2.png)

Upon reviewing all content, the client notifies users:

![Announcement upon mail reading complete](./img/mailviewer-3.png)

