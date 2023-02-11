/// <reference types="svelte" />
/// <reference types="vite/client.d.ts" />

declare namespace svelte.JSX {
    interface HTMLProps<T> {
        onautocomplete?: (event: CustomEvent) => void;
    }
}