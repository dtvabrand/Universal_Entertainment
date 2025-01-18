<?php
$id = '2Xn1Bb697A0';
$url = "https://www.youtube.com/live/$id/live";
$html = file_get_contents($url);
preg_match('/"hlsManifestUrl":"([^"]+\.m3u8)"/', $html, $matches);
echo isset($matches[1]) ? $matches[1] : 'Error: HLS manifest URL not found.';
?>
