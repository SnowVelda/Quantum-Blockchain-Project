<?php
// DEV admin panel - DO NOT expose publicly.
// Change default password immediately if you plan to use it locally.
$admin_password = getenv('ADMIN_PANEL_PASSWORD') ?: 'admin_password';
session_start();
if (isset($_POST['logout'])) { session_destroy(); header('Location: ' . $_SERVER['PHP_SELF']); exit; }
if (isset($_POST['password'])) {
    if ($_POST['password'] === $admin_password) { $_SESSION['logged_in'] = true; } else { $error = "Invalid password."; }
}
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
?>
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Admin Login</title>
<style>body{font-family:Arial;background:#f4f4f4;display:flex;align-items:center;justify-content:center;height:100vh;margin:0}form{background:#fff;padding:24px;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,0.08)}</style></head><body>
<form method="post"><h2>Admin Panel</h2><input type="password" name="password" placeholder="Password" required style="padding:8px;width:100%;margin:8px 0"><button type="submit">Login</button><?php if(isset($error)){echo '<p style="color:red">'.$error.'</p>';} ?></form>
</body></html>
<?php exit; }
// Admin logic
$output=''; $error_message='';
if (isset($_POST['action'])) {
    $action = $_POST['action'];
    $project_root = '/app'; // if inside container; adjust when deploying
    switch ($action) {
        case 'start_all': $command = "docker-compose -f {$project_root}/docker-compose.yml up --build -d"; break;
        case 'stop_all':  $command = "docker-compose -f {$project_root}/docker-compose.yml down -v"; break;
        case 'status':    $command = "docker-compose -f {$project_root}/docker-compose.yml ps"; break;
        default: $error_message = "Invalid action.";
    }
    if (!empty($command)) {
        $output = shell_exec($command . ' 2>&1');
        if ($output === null) { $error_message = "Command failed or no output. Check environment/permissions."; }
    }
}
?>
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Silver Screens Admin Panel</title></head>
<body style="font-family:Arial;margin:20px">
<form method="post"><button name="logout">Logout</button></form>
<h2>Silver Screens Admin Panel (DEV)</h2>
<p><strong>WARNING:</strong> This panel runs shell commands. Use only in local/dev environment.</p>
<form method="post">
<button name="action" value="start_all">Start All Services</button>
<button name="action" value="stop_all">Stop All</button>
<button name="action" value="status">Status</button>
</form>
<?php if($error_message) echo "<p style='color:red;'>$error_message</p>"; ?>
<?php if($output) echo "<h3>Output</h3><pre>".htmlspecialchars($output)."</pre>"; ?>
</body></html>
