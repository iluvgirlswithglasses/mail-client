import re
import base64
import os

class Separator:
    @staticmethod
    def get_boundary(content_type_header):
        boundary_start = content_type_header.find('boundary="') + len('boundary="')
        boundary_end = content_type_header.find('"', boundary_start)
        if boundary_start != -1 and boundary_end != -1:
            return content_type_header[boundary_start:boundary_end]
        else:
            return None

    @staticmethod
    def separate_attachment(data):
        attachments = []
        # Use regular expressions to extract filename and base64 content for each attachment
        matches = re.finditer(r'Content-Disposition: attachment; filename="([^"]+)"\nContent-Transfer-Encoding: base64\n\n(.+?)\n-{14}', data, re.DOTALL)

        for match in matches:
            filename = match.group(1)
            base64_content = match.group(2)
            # Can be modified to save the content into a file.type
            attachments.append((filename, base64_content))

        return attachments

    @staticmethod
    # separate message and attachments
    def separate_content(response):
        boundary = Separator.get_boundary(response)

        if not boundary:
            return response, []

        start_marker = f"--{boundary}"

        content_lines = []
        found_boundary = False

        for line in response.splitlines():
            if line.startswith(start_marker):
                if found_boundary:
                    break
                found_boundary = True
            content_lines.append(line)

        mail_content = '\n'.join(content_lines).strip()
        attachment_content = Separator.separate_attachment(response)

        return mail_content, attachment_content

    @staticmethod
    def decode_attachment(base64_content, savePath):
        with open(savePath, 'wb') as attachment_file:
            decoded_data = base64.b64decode(base64_content)
            attachment_file.write(decoded_data)

