import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
import type { PriceType } from './data'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatPrice(price: number | null, priceType: PriceType): string {
  if (priceType === 'free') return 'Free'
  if (price === null) return 'Price TBA'

  const formatted = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
  }).format(price)

  switch (priceType) {
    case 'subscription': return `${formatted}/mo`
    case 'freemium': return `Free / ${formatted}`
    case 'one-time': return formatted
    default: return formatted
  }
}

export function formatRating(rating: number): string {
  return rating.toFixed(1)
}

export function formatRatingCount(count: number): string {
  if (count >= 1000) return `${(count / 1000).toFixed(1)}k`
  return count.toString()
}

export function priceTypeBadge(priceType: PriceType): string {
  switch (priceType) {
    case 'free': return 'Free'
    case 'freemium': return 'Freemium'
    case 'one-time': return 'One-time'
    case 'subscription': return 'Subscription'
  }
}
