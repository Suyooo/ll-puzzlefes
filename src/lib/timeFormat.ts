export function timeFormat(ms: number): string {
    const s = Math.floor(ms / 1000);
    const m = Math.floor(s / 60);
    const printS = s % 60;

    if (m < 60) {
        return `${m < 10 ? "0" : ""}${m}:${printS < 10 ? "0" : ""}${printS}`;
    } else {
        const h = Math.floor(m / 60);
        const printM = m % 60;
        return `${h}:${printM < 10 ? "0" : ""}${printM}:${printS < 10 ? "0" : ""}${printS}`;
    }
}