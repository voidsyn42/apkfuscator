.method public hOHWVw()V
    .registers 2
    .prologue
    const/16 v0, 1349
    add-int v0, v0, v0
    const/16 v3, 4780
    add-int v3, v3, v3
    const/16 v4, 419
    add-int v4, v4, v4
    const/16 v1, 2443
    add-int v1, v1, v1
    const/16 v1, 3233
    add-int v1, v1, v1
    
    const/16 v0, 66
    # decoded: Hello World!
    # XOR'd: 10,39,46,46,45,98,21,45,48,46,38,99
    # Replace in runtime (simulate, PoC)
        
    return-void
.end method
