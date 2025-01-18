<?php
$id = '2Xn1Bb697A0'; // ID del video che hai fornito
$url = "https://www.youtube.com/live/$id/live";

$html = file_get_contents($url);
if ($html === false) {
    echo "Error: Unable to fetch the URL.";
    exit;
}

// Stampa il contenuto HTML per la verifica
echo htmlspecialchars($html);

preg_match('/"hlsManifestUrl":"([^"]+\.m3u8)"/', $html, $matches);
$stream_url = isset($matches[1]) ? $matches[1] : '';

if (!empty($stream_url)) {
    echo $stream_url;
} else {
    echo "Error: HLS manifest URL not found.";
}
?>
