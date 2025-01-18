package main

import (
    "context"
    "encoding/json"
    "fmt"
    "github.com/chromedp/chromedp"
    "os"
    "path/filepath"
)

func main() {
    // Crea il contesto
    ctx, cancel := chromedp.NewContext(context.Background())
    defer cancel()

    // Avvia Chrome
    if err := chromedp.Run(ctx, chromedp.Navigate("https://www.youtube.com")); err != nil {
        fmt.Println("Errore durante la navigazione:", err)
        os.Exit(1)
    }

    // Aspetta qualche secondo per assicurarsi che la pagina si carichi
    chromedp.Sleep(10)

    // Estrai i cookie
    var cookies []byte
    if err := chromedp.Run(ctx, chromedp.ActionFunc(func(ctx context.Context) error {
        var err error
        cookies, err = chromedp.Cookie()
        return err
    })); err != nil {
        fmt.Println("Errore durante l'estrazione dei cookie:", err)
        os.Exit(1)
    }

    // Salva i cookie in formato Mozilla/Netscape
    var cookieMap []map[string]interface{}
    if err := json.Unmarshal(cookies, &cookieMap); err != nil {
        fmt.Println("Errore durante l'analisi dei cookie:", err)
        os.Exit(1)
    }

    file, err := os.Create(filepath.Join("scripts", "cookies.txt"))
    if err != nil {
        fmt.Println("Errore durante la creazione del file:", err)
        os.Exit(1)
    }
    defer file.Close()

    file.WriteString("# Netscape HTTP Cookie File\n")
    for _, cookie := range cookieMap {
        file.WriteString(fmt.Sprintf("%s\tTRUE\t%s\t%s\t%d\t%s\t%s\n",
            cookie["domain"], cookie["path"], cookie["secure"], cookie["expires"], cookie["name"], cookie["value"]))
    }

    fmt.Println("Cookie estratti e salvati con successo.")
}
