import { ErrorBoundary, ErrorFallback } from '@components/common';
import { LazyMotionProvider } from '@components/common/LazyMotionProvider';
import { microDampingPreset } from '@constants/anim/spring';
import { friendsData } from '@constants/friends-config';
import { m } from 'motion/react';
import FriendCard from './FriendCard';

// Map specific category icons matching Japanese anime / Ghibli botanical theme
const categoryIcons: Record<string, { icon: string; label: string; color: string }> = {
  'Finansial & Syariah': {
    icon: 'ri:scales-3-line',
    label: 'Syariah & Fiqh',
    color: '#4A7C59',
  },
  'Bisnis & UMKM': {
    icon: 'ri:store-2-line',
    label: 'Bisnis & UMKM',
    color: '#E07A5F',
  },
  'Investasi & Pasar Modal': {
    icon: 'ri:line-chart-line',
    label: 'Pasar Modal',
    color: '#2A9D8F',
  },
  'Tools Multimedia & Utilitas': {
    icon: 'ri:magic-line',
    label: 'Multimedia & Utilitas',
    color: '#8338EC',
  },
};

export default function FriendsGrid() {
  // Group friends by category
  const categoriesMap = friendsData.reduce<Record<string, typeof friendsData>>((acc, item) => {
    const cat = item.category || 'Lainnya';
    if (!acc[cat]) {
      acc[cat] = [];
    }
    acc[cat].push(item);
    return acc;
  }, {});

  const categoryNames = Object.keys(categoriesMap);

  return (
    <LazyMotionProvider>
      <ErrorBoundary FallbackComponent={ErrorFallback}>
        <div className="flex w-full flex-col gap-10">
          {categoryNames.map((catName) => {
            const items = categoriesMap[catName];
            const meta = categoryIcons[catName] || {
              icon: 'ri:apps-2-line',
              label: catName,
              color: '#3D5A80',
            };

            return (
              <div key={catName} className="flex flex-col gap-4">
                {/* Section Category Header with Aesthetic Decorative Icon & Pill Badge */}
                <div className="flex items-center justify-between border-gray-200/60 border-b pb-3 dark:border-gray-800/80">
                  <div className="flex items-center gap-3">
                    {/* Decorative Ghibli-themed Icon Container */}
                    <div
                      className="flex h-8 w-8 items-center justify-center rounded-xl shadow-xs transition-transform duration-300 hover:scale-105"
                      style={{
                        background: `linear-gradient(135deg, ${meta.color}25, ${meta.color}10)`,
                        border: `1px solid ${meta.color}40`,
                        color: meta.color,
                      }}
                    >
                      <i className={`${meta.icon} text-lg`} />
                    </div>

                    {/* Category Title */}
                    <h2 className="font-bold text-gray-900 text-lg tracking-tight dark:text-white">{catName}</h2>
                  </div>

                  {/* Subtle Subtitle / Tool Count Pill */}
                  <div
                    className="flex items-center gap-1.5 rounded-full px-3 py-1 font-medium text-xs"
                    style={{
                      background: `linear-gradient(135deg, ${meta.color}15, transparent)`,
                      border: `1px solid ${meta.color}25`,
                      color: meta.color,
                    }}
                  >
                    <span className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: meta.color }} />
                    <span>{items.length} Tools</span>
                  </div>
                </div>

                {/* Grid Container */}
                <div className="grid grid-cols-3 gap-6 md:grid-cols-2 md:gap-4 xl:grid-cols-4 xl:gap-8">
                  {items.map((friend, index) => (
                    <FriendCard key={friend.url} friend={friend} index={index} />
                  ))}
                </div>
              </div>
            );
          })}

          {/* Empty State */}
          {friendsData.length === 0 && (
            <m.div
              className="flex min-h-[300px] flex-col items-center justify-center text-center"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, ...microDampingPreset }}
            >
              <h3 className="mb-2 font-bold text-3xl text-gray-700 dark:text-gray-300">The Void is Empty</h3>
              <p className="text-gray-500 text-lg dark:text-gray-400">Be the first to connect!</p>
            </m.div>
          )}
        </div>
      </ErrorBoundary>
    </LazyMotionProvider>
  );
}
