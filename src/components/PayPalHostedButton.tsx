// src/components/PayPalHostedButton.tsx
import React, { useEffect, useRef, useState } from 'react';

type PayPalHostedButtonProps = {
    hostedButtonId: string;
    containerId?: string; // 任意で指定。未指定なら自動生成
};

const PayPalHostedButton: React.FC<PayPalHostedButtonProps> = ({
    hostedButtonId,
    containerId,
}) => {
    const [scriptLoaded, setScriptLoaded] = useState(false);
    const internalId = useRef(containerId || `paypal-container-${hostedButtonId}`);

    // PayPalスクリプトを1度だけグローバルに読み込む
    useEffect(() => {
        // SSR環境では実行しない
        if (typeof window === 'undefined') return;
        if ((window as any).paypal?.HostedButtons) {
            setScriptLoaded(true);
            return;
        }

        // すでに読み込み中のスクリプトがあるかを確認
        const existingScript = document.querySelector<HTMLScriptElement>(
            'script[src^="https://www.paypal.com/sdk/js?client-id=BAAtig5X1urW0ewb5Hn3iEPaMPjuQ1QYYQ7m3k6Cacv_bsJejaQDRPNC7TINvhCIMaZ_txDGj6kU9A9xBQ&components=hosted-buttons&disable-funding=venmo&currency=JPY"]'
        );
        if (existingScript) {
            existingScript.addEventListener('load', () => setScriptLoaded(true));
            return;
        }

        const script = document.createElement('script');
        script.src = "https://www.paypal.com/sdk/js?client-id=BAAtig5X1urW0ewb5Hn3iEPaMPjuQ1QYYQ7m3k6Cacv_bsJejaQDRPNC7TINvhCIMaZ_txDGj6kU9A9xBQ&components=hosted-buttons&disable-funding=venmo&currency=JPY";
        script.async = true;
        script.onload = () => setScriptLoaded(true);
        document.body.appendChild(script);

        return () => {
            script.onload = null;
        };
    }, [hostedButtonId]);

    // PayPalボタンのレンダリング
    useEffect(() => {
        if (scriptLoaded && (window as any).paypal?.HostedButtons) {
            (window as any).paypal.HostedButtons({
                hostedButtonId,
            }).render(`#${internalId.current}`);
        }
    }, [scriptLoaded, hostedButtonId]);

    return <div id={internalId.current} />;
};

export default PayPalHostedButton;
