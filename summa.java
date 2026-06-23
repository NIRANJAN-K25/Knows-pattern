for(int i = 0; i < n; i++) {
    arr[i]--;
}

for(int i = 0; i < n; i++) {
    arr[arr[i] % n] += n;
}

for(int i = 0; i < n; i++) {
    arr[i] /= n;
}