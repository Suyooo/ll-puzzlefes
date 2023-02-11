import {writable} from "svelte/store";

export interface PuzzleState {
    solved: boolean,
    totalTime: number,
    wrongGuesses: string[]
}

export const STATES = writable<{ [key: string]: PuzzleState }>(
    JSON.parse(localStorage.getItem("llpuzzle-states")) ?? {});

STATES.subscribe(states => {
    localStorage.setItem("llpuzzle-states", JSON.stringify(states));
});

export function createState(key: string) {
    STATES.update(states => {
        states[key] = {
            solved: false,
            totalTime: 0,
            wrongGuesses: []
        };
        return states;
    });
}

let activeTimerKey: string | null = null;
let activeTimerStart: number = 0;

export function startTimer(key: string) {
    endTimer();
    activeTimerKey = key;
    activeTimerStart = Date.now();
}

export function endTimer() {
    if (activeTimerKey === null) return;
    const key = activeTimerKey;
    const elapsedTime = Date.now() - activeTimerStart;
    activeTimerKey = null;

    STATES.update(states => {
        states[key].totalTime += elapsedTime;
        return states;
    });
}

window.onbeforeunload = endTimer;