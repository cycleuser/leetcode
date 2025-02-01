html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>502 Bad Gateway Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
        }
        .cf-error-details-wrapper {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .cf-status-item {
            display: inline-block;
            margin-right: 20px;
        }
        .cf-icon-error-container {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .cf-icon-ok {
            color: green;
        }
        .cf-icon-error {
            color: red;
        }
    </style>
</head>
<body>
    <div id="cf-wrapper">
        <div id="cf-error-details" class="cf-error-details-wrapper">
            <h1>Error 502 Bad Gateway</h1>
            <small>Ray ID: 52beb9bebad1d8bd &bull; 2019-10-26 19:09:36 UTC</small>
            <h2 class="cf-subheadline">What happened?</h2>
            <p>The web server reported a bad gateway error.</p>
            <h2 class="cf-subheadline">What can I do?</h2>
            <p>Please try again in a few minutes.</p>
            
            <div class="cf-section cf-highlight cf-status-display">
                <div id="cf-browser-status" class="cf-column cf-status-item cf-browser-status">
                    <div class="cf-icon-error-container">
                        <i class="cf-icon cf-icon-browser"></i>
                        <i class="cf-icon-status cf-icon-ok"></i>
                    </div>
                    <span class="cf-status-desc">You</span>
                    <h3 class="cf-status-name">Browser</h3>
                    <span class="cf-status-label">Working</span>
                </div>
                
                <div id="cf-cloudflare-status" class="cf-column cf-status-item cf-cloudflare-status">
                    <div class="cf-icon-error-container">
                        <i class="cf-icon cf-icon-cloud"></i>
                        <i class="cf-icon-status cf-icon-ok"></i>
                    </div>
                    <span class="cf-status-desc">Amsterdam</span>
                    <h3 class="cf-status-name">Cloudflare</h3>
                    <span class="cf-status-label">Working</span>
                </div>
                
                <div id="cf-host-status" class="cf-column cf-status-item cf-host-status cf-error-source">
                    <div class="cf-icon-error-container">
                        <i class="cf-icon cf-icon-server"></i>
                        <i class="cf-icon-status cf-icon-error"></i>
                    </div>
                    <span class="cf-status-desc">leetcode.com</span>
                    <h3 class="cf-status-name">Host</h3>
                    <span class="cf-status-label">Error</span>
                </div>
            </div>
            
            <div class="cf-error-footer cf-wrapper">
                <p>Cloudflare Ray ID: 52beb9bebad1d8bd
                    &bull; Your IP: 92.44.160.241
                    &bull; Performance & security by Cloudflare</p>
            </div>
        </div>
    </div>
</body>
</html>
