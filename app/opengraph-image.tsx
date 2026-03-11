import { ImageResponse } from 'next/og'

export const alt = 'Audio Software Hub — The Definitive Music Production Directory'
export const size = { width: 1200, height: 630 }
export const contentType = 'image/png'

export default async function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          background: '#000000',
          width: '100%',
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          padding: '80px',
          fontFamily: 'sans-serif',
        }}
      >
        {/* Top bar */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#ffffff' }} />
          <span style={{ color: 'rgba(255,255,255,0.4)', fontSize: '14px', letterSpacing: '0.2em', textTransform: 'uppercase' }}>
            Audio Software Hub
          </span>
        </div>

        {/* Main headline */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          <div
            style={{
              color: '#ffffff',
              fontSize: '80px',
              fontWeight: 300,
              lineHeight: 1.05,
              letterSpacing: '-0.03em',
            }}
          >
            Find the audio tool
          </div>
          <div
            style={{
              color: 'rgba(255,255,255,0.5)',
              fontSize: '80px',
              fontWeight: 400,
              fontStyle: 'italic',
              lineHeight: 1.05,
              letterSpacing: '-0.03em',
            }}
          >
            you need today
          </div>
        </div>

        {/* Bottom stats */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '48px' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <span style={{ color: '#ffffff', fontSize: '32px', fontWeight: 300 }}>3,000+</span>
            <span style={{ color: 'rgba(255,255,255,0.3)', fontSize: '11px', letterSpacing: '0.15em', textTransform: 'uppercase' }}>
              Music Tools
            </span>
          </div>
          <div style={{ width: '1px', height: '48px', background: 'rgba(255,255,255,0.1)' }} />
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <span style={{ color: '#ffffff', fontSize: '32px', fontWeight: 300 }}>150+</span>
            <span style={{ color: 'rgba(255,255,255,0.3)', fontSize: '11px', letterSpacing: '0.15em', textTransform: 'uppercase' }}>
              Manufacturers
            </span>
          </div>
          <div style={{ width: '1px', height: '48px', background: 'rgba(255,255,255,0.1)' }} />
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <span style={{ color: '#ffffff', fontSize: '32px', fontWeight: 300 }}>24/7</span>
            <span style={{ color: 'rgba(255,255,255,0.3)', fontSize: '11px', letterSpacing: '0.15em', textTransform: 'uppercase' }}>
              Updated
            </span>
          </div>
        </div>
      </div>
    ),
    { ...size }
  )
}
